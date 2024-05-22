from flask import Blueprint, request, jsonify
from models.tarea_model import Tarea
from views.tarea_view import render_tarea_list, render_tarea_detail
from utils.decorators import jwt_required, roles_required

tarea_bp = Blueprint("tarea", __name__)

@tarea_bp.route("/tareas", methods=["GET"])
@jwt_required
@roles_required(roles="admin" or "member")
def get_all():
    tareas = Tarea.get_all()
    return jsonify(render_tarea_list(tareas))

@tarea_bp.route("/tareas/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles="admin" or "member")
def get_by_id(id):
    tarea = Tarea.get_by_id(id)
    if tarea:
        return jsonify(render_tarea_detail(tarea))
    return jsonify({"error": " no encontrado"}), 404

@tarea_bp.route("/tareas", methods=["POST"])
@jwt_required
@roles_required(roles="admin")
def create_tarea():
    data = request.json
    title = data.get("title")
    description = data.get("description")
    status = data.get("status")
    created_at = data.get("created_at")
    assigned_to = data.get("assigned_to")
    
    if not title or not description or not status or not created_at or not assigned_to:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    tarea = Tarea(title=title)
    tarea.save()

    return jsonify(render_tarea_detail()), 201


@tarea_bp.route("/tareas/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles="admin")
def update_tarea(id):
    tarea = Tarea.get_by_id(id)

    if not tarea:
        return jsonify({"error": " no encontrado"}), 404

    data = request.json
    title = data.get("title")
    description = data.get("description")
    status = data.get("status")
    created_at = data.get("created_at")
    assigned_to = data.get("assigned_to")

    tarea.update(title=title, description=description, status=status, created_at=created_at, assigned_to=assigned_to)

    return jsonify(render_tarea_detail())


@tarea_bp.route("/tareas/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles="admin")
def delete_tarea(id):
    tarea = Tarea.get_by_id(id)
    if not tarea:
        return jsonify({"error": " no encontrado"}), 404

    tarea.delete()
    return "", 204