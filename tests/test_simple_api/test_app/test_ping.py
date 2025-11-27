from src.simple_api.core import StatusCode, HTTPMethod, Response


async def test_app_ping(app, client):
    @app.add_route('/ping', HTTPMethod.GET)
    async def _():
        return Response(StatusCode.OK, 'pong')

    # Стартуем после роутинга
    await app.start(port=8080)
    try:
        response = await client(HTTPMethod.GET, '/ping')

        assert response.status == StatusCode.OK
        assert await response.text() == 'pong'
    finally:
        await app.shutdown()
