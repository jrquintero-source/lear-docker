#!/bin/sh

echo "Iniciando contenedor..."

# comportamiento dinámico según entorno
if [ "$APP_ENV" = "prod" ]; then
export DEBUG=false
else
export DEBUG=true
fi

# ejecuta el comando final
exec "$@"