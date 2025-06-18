import time
import random
from mathquiz.operations import OPERATIONS
import csv

class Question:
    def __init__(self, a, b, op, decimals):
        self.a = round(a, decimals) if decimals else int(a)
        self.b = round(b, decimals) if decimals else int(b)
        self.op = OPERATIONS[op]

    def text(self):
        return f"{self.a} {self.op.symbol} {self.b} = ?"

    def answer(self):
        return round(self.op.apply(self.a, self.b), 2)

class Quiz:
    def __init__(self, args):
        self.num = args.num
        self.ops = args.ops
        self.min = args.min
        self.max = args.max
        self.decimals = args.decimals
        self.places = args.places
        self.results = []

    def run(self):
        print("Iniciando o quiz matemático!\n")
        start_time = time.time()

        for i in range(1, self.num + 1):
            a = random.uniform(self.min, self.max)
            b = random.uniform(self.min, self.max)
            op = random.choice(self.ops)
            q = Question(a, b, op, self.places if self.decimals else 0)

            print(f"Questão {i}: {q.text()}")
            try:
                user_answer = float(input("> "))
                correct = abs(user_answer - q.answer()) < 0.01
            except Exception:
                correct = False
            self.results.append((q, correct))
            print("Correto!\n" if correct else f"Errado. Resposta correta: {q.answer()}\n")

        total_time = time.time() - start_time
        correct_count = sum(1 for _, c in self.results if c)

        print("Resultado Final")
        print("------------------")
        print(f"Total: {self.num} questões")
        print(f"Corretas: {correct_count}")
        print(f"Incorretas: {self.num - correct_count}")
        print(f"% Acerto: {100 * correct_count / self.num:.2f}%")
        print(f"Tempo total: {total_time:.2f}s")
        print(f"Tempo médio por questão: {total_time / self.num:.2f}s")
        with open("resultados.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Pergunta", "Resposta correta", "Acertou?"])
            for q, c in self.results:
                writer.writerow([q.text(), q.answer(), "Sim" if c else "Não"])
        print("Resultados salvos em 'resultados.csv'.")
        print("Quiz concluído! Obrigado por participar.")