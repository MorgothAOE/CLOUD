from src.web import create_app

# APP PARA DESARROLLO
app = create_app()

if __name__ == '__main__':
    app.run()