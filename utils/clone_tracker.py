import platform
payload = {
    "repo": "beyond-the-mirror",
    "timestamp": datetime.utcnow().isoformat(),
    "system": platform.system(),
    "release": platform.release()
}
        requests.post("https://maker.ifttt.com/trigger/clone_event/with/key/YOUR_KEY", json=payload)
    except Exception:
        pass  # Fails silently so it doesn't break anything
