from flask import Blueprint, request, jsonify
from app.services import factorial, fibonacci, power
from app.models import OperationInput, OperationRequest
from app.database import SessionLocal


math_bp = Blueprint("math", __name__)


@math_bp.route("/api/compute", methods=["POST"])
def compute():
    data = request.get_json()
    parsed = OperationInput(**data)
    session = SessionLocal()

    try:
        if parsed.operation == "factorial":
            result = factorial(parsed.number)
        elif parsed.operation == "fibonacci":
            result = fibonacci(parsed.number)
        elif parsed.operation == "power":
            result = power(parsed.number)
        else:
            return jsonify({"error": "Invalid operation"}), 400

        record = OperationRequest(
            operation=parsed.operation,
            input=str(parsed.number),
            result=str(result),
        )
        session.add(record)
        session.commit()
        return jsonify({"result": result})
    finally:
        session.close()
