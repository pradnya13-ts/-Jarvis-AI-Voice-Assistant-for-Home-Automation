import pywhatkit
import datetime


def send_whatsapp_message(contact_name, message):
    # Convert all contact names to lowercase internally
    contacts = {
        "mom": "+919972904860",
        "dad": "+918150004624",
        "madiha": "+918105827276",
        "yuvi": "+919527248908",
        "purvi": "+918010228610",
        "nagamma": "+919916401853"

    }

    contact_name = contact_name.lower().strip()

    if contact_name not in contacts:
        return f"❌ I don't have the number for {contact_name.title()}."

    phone = contacts[contact_name]
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 2
    if minute >= 60:
        minute -= 60
        hour = (hour + 1) % 24

    try:
        pywhatkit.sendwhatmsg(phone, message, hour, minute)
        return f"✅ Message scheduled to {contact_name.title()} at {hour}:{minute:02d}."
    except Exception as e:
        return f"⚠️ Failed to send message: {str(e)}"


