from flask import Blueprint, request, jsonify
from model.predio import Predio
from utils.db import db

predios=Blueprint('predios',__name__)

@predios.route('/predios/v0',methods=['GET'])
def getMensaje():
    result={}
    result["data"]='flask-crud-backend'
    return jsonify(result)

@predios.route('/predios/v0/listar',methods=['GET'])
def getPredios():
    result={}
    predios=Predio.query.all()    
    result["data"]=predios
    result["status_code"]=200
    result["msg"]="Se recupero los predios sin inconvenientes"
    return jsonify(result),200

@predios.route('/predios/v0/insert',methods=['POST'])
def insert():
    result={}
    body=request.get_json()
    id_tipo_predio=body.get("id_tipo_predio")
    descripcion=body.get("descripcion")
    ruc=body.get("ruc")
    telefono=body.get("telefono")
    correo=body.get("correo")
    direccion=body.get("direccion")
    idubigeo=body.get("idubigeo")
    id_persona=body.get("id_persona")
    url_imagen=body.get("url_imagen")

    if not id_tipo_predio or not descripcion or not ruc or not telefono or not correo or not direccion or not idubigeo or not id_persona or not url_imagen:
        result["status_code"]=400
        result["msg"]="Faltan datos"
        return jsonify(result), 400
    
    predio=Predio(id_tipo_predio,descripcion,ruc,telefono,correo,direccion,idubigeo,id_persona,url_imagen)
    db.session.add(predio)
    db.session.commit()
    result["data"]=predio
    result["status_code"]=201
    result["msg"]="Se agrego correctamente"
    return jsonify(result), 201



