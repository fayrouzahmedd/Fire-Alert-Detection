import time

class AlertTracker:
    def __init__(self, cooldown=5):
        self.last_alert_time = 0
        self.cooldown = cooldown

    def should_alert(self):
        now = time.time()
        if now - self.last_alert_time > self.cooldown:
            self.last_alert_time = now
            return True
        return False