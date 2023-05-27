import httpx

class APICaller:

    async def api_call_get(url, query_params):
        async with httpx.AsyncClient() as client:
            url = url + query_params
            response = await client.get(url)
            return response