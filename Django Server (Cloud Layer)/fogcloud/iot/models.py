from django.db import models

class SensorData(models.Model):
    node_id = models.CharField(max_length=50)
    humidity = models.FloatField()
    temperature = models.FloatField()
    fan_level = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.node_id} - {self.temperature}°C / {self.humidity}%"
