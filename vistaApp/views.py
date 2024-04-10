from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("""
    <style>
    body {
        background-color: #F7C566;
    }
    h1 {
        margin-top: 50px;
        font-size: 50px;
        text-align: center;
        color: #6C0345;
    }
    
        p {
        margin-left:   200px;
        margin-bottom: 150px;
        font-size: 30px;
        font-weight: bold;
        color: #FF204E;
        
    }
    
    h2 {
        text-align: center;
        color: #362FD9;
        
    }
    
    .paginas {
        text-align: center;
        font-size: 25px;
    }    
    </style>
    
    <h1>Bienvenido al Home</h1>
    <p>Esta es la pagina de inicio</p>

    <h2>Visita las siguientes paginas:</h2>
    <div class="paginas">
        <a href="/about/">About</a>
        <a href="/contact/">Contact</a>
    <div/>
    """)
    
def about(request):
    return HttpResponse("""
    <style>
    body {
        background-color: #FFC6AC;
    }
    h1 {
        margin-top: 50px;
        font-size: 50px;
        text-align: center;
        color: #068FFF;
    }
    
        p {
        margin-left:   200px;
        margin-bottom: 150px;
        font-size: 30px;
        font-weight: bold;
        color: #FF204E;
        
    }
    
    .paginas {
        text-align: center;   
        font-size: 25px;
    }    
    </style>
    
    <h1>Bienvenido al About</h1>
    <p> Esta es la pagina de about</p>
    <div class="paginas">
        <a href="/">Home</a>
        <a href="/contact/">Contact</a>
    <div>
    """)

def contact(request):
    return HttpResponse("""
     <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contacto</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #47A992;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            margin: 50px auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input[type="text"],
        input[type="email"],
        textarea {
            width: calc(100% - 10px);
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }
        button {
            padding: 10px 20px;
            background-color: #007BFF;
            color: #fff;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056B3;
        }
        button:focus {
            outline: none;
        }
        .paginas {
        text-align: center;   
        font-size: 25px;
    } 
    </style>
</head>
<body>
    <div class="container">
        <h1>Contacto</h1>
        <form action="#" method="post">
            <div class="form-group">
                <label for="nombre">Nombre:</label>
                <input type="text" id="nombre" name="nombre" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="mensaje">Mensaje:</label>
                <textarea id="mensaje" name="mensaje" rows="4" required></textarea>
            </div>
            <button type="submit">Enviar</button>
        </form>
    </div>
        <div class="paginas">
        <a href="/">Home</a>
        <a href="/about/">About</a>
    <div>
</body>
</html>
""")