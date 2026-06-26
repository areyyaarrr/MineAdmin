from mcstatus import JavaServer

def get_server_status():
    try:
        server = JavaServer.lookup("localhost:25565")
        status = server.status()
        return {
            "online": True,
            "players": status.players.online,
            "max_players": status.players.max,
            "latency": status.latency,
            "motd": status.description,
        }
    except Exception:
        return {"online": False}
