import asyncio

def send_order_email(order_id: int, email: str):
    # Mocks sending email
    print(f"[MOCK EMAIL] Sent confirmation for order {order_id} to {email}")
    # Actually sleeping for demonstration
    asyncio.run(asyncio.sleep(0.1))
