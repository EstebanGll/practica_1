import random, sys;

 # Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
    "// Esto es un comentario",
    "/* Esto es un comentario */",
    "-- Esto es un comentario",
    "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1];

puntaje = 0;

# El usuario deberá contestar 3 preguntas, question_to_ask creo una lista que contiene a todas
questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3);


#k hace que se seleccionen 3 valores de las que estan conformadas sus listas internas

for question, options, correct_answer in questions_to_ask:
    
    # Se muestra la pregunta y las respuestas posibles
    print(question);
    for i, answer in enumerate(options):
        print(f"{i + 1}. {answer}");
       
# El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        respuesta = input("Respuesta: ");
        
        ### verifica si es un digito entre 1 a 4 o sale del programa
        if respuesta.isdigit():
            if int(respuesta) >= 1 and int(respuesta) <= 4:
                user_answer = int(respuesta)-1;
            else:
                print("Respuesta no valida");
                sys.exit(1);
        else:
            print("Respuesta no valida");
            sys.exit(1);
            
        
        # Se verifica si la respuesta es correcta
        if user_answer == correct_answer:
            puntaje += 1;
            print("¡Correcto!");
            break;
        else:
            puntaje -= 0.5;
    else:
    # Si el usuario no responde correctamente después de 2 intentos,
    # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:");
        print(options[correct_answer]);
# Se imprime un blanco al final de la pregunta
print("Obtuvo un puntaje de:",puntaje);