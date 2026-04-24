from django.db import models
from django.contrib.auth.models import User
from core.shared.models import TimestampedModel


class ChatRoom(TimestampedModel):
    """Chat room between patient and doctor."""
    
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='chat_rooms_as_patient')
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE, related_name='chat_rooms_as_doctor')
    appointment = models.OneToOneField('appointments.Appointment', on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = [['patient', 'doctor']]
    
    def __str__(self):
        return f"Chat: {self.patient.user.username} - {self.doctor.user.username}"


class Message(TimestampedModel):
    """Message model."""
    
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    attachment = models.FileField(upload_to='chat_attachments/', null=True, blank=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f"Message from {self.sender.username} in {self.chat_room}"
