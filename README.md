# 🎬 CRUD de Películas con Flask 🎥

Este es un proyecto básico que implementa un **CRUD de películas** utilizando Flask. ¡Es ideal para aprender los fundamentos de las API REST y cómo integrarlas con una vista HTML minimalista! 🌟

## 🚀 Funcionalidades
- **Crear** una nueva película. 🆕
- **Leer** la lista de películas. 📜
- **Actualizar** los detalles de una película. 🔄
- **Eliminar** una película. 🗑️

---

## 📂 Estructura del Proyecto

```
ApiRestPython/
├── app/
│   ├── server.py        # Servicio Flask
│   ├── static/
│   │   └── styles.css   # Estilo CSS
│   └── templates/
│       └── index.html   # Vista HTML
│
├── README.md            # Descripción del proyecto
└── requirements.txt     # Dependencias de Python
```

---

## 🛠️ Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/millanda29/ApiRestPython.git
   cd ApiRestPython
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # En Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Genera el archivo `requirements.txt` si no existe:
   ```bash
   pip freeze > requirements.txt
   ```

---

## ▶️ Ejecución

Ejecuta el servidor Flask con el siguiente comando:

```bash
python app/server.py
```

Abre tu navegador en [http://127.0.0.1:5000](http://127.0.0.1:5000) y disfruta de la aplicación. 🌐

---

## 📸 Vista Previa

![Vista de la Aplicación](https://via.placeholder.com/800x400?text=Preview)

---

## 📝 Notas

- Puedes personalizar las películas iniciales editando el diccionario en `server.py`.
- ¡Prueba las rutas de la API usando herramientas como Postman o cURL! 🤓
