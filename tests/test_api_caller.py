import pytest
import httpx


@pytest.mark.asyncio
async def test_api_call_get():
    url = "https://jsonplaceholder.typicode.com/posts"
    query_params = "?userId=1"

    async with httpx.AsyncClient() as client:
        url = url + query_params
        response = await client.get(url)

    assert response.status_code == 200
    assert response.json() is not None
