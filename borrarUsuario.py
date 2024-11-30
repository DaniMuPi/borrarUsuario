from cargarUsuarios import cargarUsuarios

def borrarUsuario(nombreUsuario, contraseñaUsuario, archivoUsuarios):
    usuarios_dict = cargarUsuarios(archivoUsuarios)
    if (nombreUsuario in usuarios_dict):
        if (usuarios_dict[nombreUsuario] == contraseñaUsuario):
            del usuarios_dict[nombreUsuario]
            with open(archivoUsuarios, 'w') as f:
                for usuario_guardado, contraseña in usuarios_dict.items():
                    f.write(f"{usuario_guardado};{contraseña}\n")
            mensaje = "Usuario eliminado correctamente."
        else:
            mensaje = "No se ha podido eliminar el usuario. Contraseña incorrecta."
    else:
        mensaje = "Este usuario no esta registrado."
    return mensaje

