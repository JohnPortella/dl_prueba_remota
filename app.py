from db import Database
from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/proyecto/<id_proyecto>')
def project(id_proyecto):
    db = Database('db/sitio.db')
    ## proyectos ##
    query_string = "SELECT * from project where INSTR(project_name , '{0}') > 0".format(id_proyecto)      
    proyectos = db.query(query_string, True)
    # limpieza - crear dict desde string
    for proyecto in proyectos:
        print(proyecto['project_images'])
        proyecto['project_images'] = json.loads(proyecto['project_images'])
    ## usuarios ##
    query_string = "SELECT u.id user_id, u.username, u.password, u.profile_picture, u.user_full_name, " \
                   "r.id role_id, r.name role_name, r.description role_description " \
                   "from user u, user_role_association_table ura, role r " \
                   "WHERE u.id = ura.user_id and ura.role_id = r.id"        
    usuarios = db.query(query_string, True)    
    # limpieza - homogeneizar el typo de password 
    for usuario in usuarios:        
        if isinstance(usuario['password'], bytes):
            usuario['password'] = usuario['password'].decode('utf-8')
    # integracion
    data = { "proyectos" : proyectos, "usuarios" : usuarios}
    # cerrar db
    db.close()    
    # conversion a json y retorno al cliente
    return jsonify(data)     
    


                    





    return 'Hello, World! ' + str(id_proyecto)

if __name__ == "__main__":
    app.run(debug=True)
