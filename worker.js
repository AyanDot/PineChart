// Cloudflare Worker: PineChart Demo Download Counter
// KV Binding: DEMO_DOWNLOADS
//
// Endpoints:
//   POST /track   — record a download (stores country + timestamp)
//   GET  /stats   — return total count + country breakdown
//
// Setup:
//   1. Create a KV namespace called "DEMO_DOWNLOADS"
//   2. Create a Worker, paste this code
//   3. In Worker Settings > Variables > KV Namespace Bindings:
//      Variable name: DEMO_DOWNLOADS  →  select your KV namespace
//   4. Deploy

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const cors = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    };

    // Handle CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: cors });
    }

    // POST /track — record a download
    if (url.pathname === '/track' && request.method === 'POST') {
      // Get country from Cloudflare (no IP stored)
      const country = request.cf?.country || 'Unknown';
      const timestamp = new Date().toISOString();

      // Increment total count
      const currentCount = parseInt(await env.DEMO_DOWNLOADS.get('total') || '0');
      await env.DEMO_DOWNLOADS.put('total', String(currentCount + 1));

      // Increment country count
      const countryKey = `country:${country}`;
      const countryCount = parseInt(await env.DEMO_DOWNLOADS.get(countryKey) || '0');
      await env.DEMO_DOWNLOADS.put(countryKey, String(countryCount + 1));

      // Append to recent downloads log (keep last 100)
      let recent = JSON.parse(await env.DEMO_DOWNLOADS.get('recent') || '[]');
      recent.unshift({ country, timestamp });
      if (recent.length > 100) recent = recent.slice(0, 100);
      await env.DEMO_DOWNLOADS.put('recent', JSON.stringify(recent));

      return new Response(JSON.stringify({ ok: true, total: currentCount + 1 }), {
        headers: { 'Content-Type': 'application/json', ...cors },
      });
    }

    // GET /stats — return all data
    if (url.pathname === '/stats' && request.method === 'GET') {
      const total = parseInt(await env.DEMO_DOWNLOADS.get('total') || '0');
      const recent = JSON.parse(await env.DEMO_DOWNLOADS.get('recent') || '[]');

      // Collect all country keys
      const list = await env.DEMO_DOWNLOADS.list({ prefix: 'country:' });
      const countries = {};
      for (const key of list.keys) {
        const name = key.name.replace('country:', '');
        countries[name] = parseInt(await env.DEMO_DOWNLOADS.get(key.name) || '0');
      }

      return new Response(JSON.stringify({ total, countries, recent }), {
        headers: { 'Content-Type': 'application/json', ...cors },
      });
    }

    return new Response('Not found', { status: 404, headers: cors });
  },
};
