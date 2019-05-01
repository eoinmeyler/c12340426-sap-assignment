# Used https://stackoverflow.com/questions/33029168/how-to-calculate-an-equation-in-a-string-python?rq=1 for calculator

import speech_recognition as stt
from gtts import gTTS
import os
import ast
import operator

_OP_MAP = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Invert: operator.neg,
}


class Calc(ast.NodeVisitor):

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return _OP_MAP[type(node.op)](left, right)

    def visit_Num(self, node):
        return node.n

    def visit_Expr(self, node):
        return self.visit(node.value)

    @classmethod
    def evaluate(cls, expression):
        tree = ast.parse(expression)
        calc = cls()
        return calc.visit(tree.body[0])


done = False
r = stt.Recognizer()
#r.adjust_for_ambient_noise


def synthesis(speech):
    outbuffer = "speech-buffer.mp3"
    tts = gTTS(speech)
    tts.save(outbuffer)
    os.system(outbuffer)


def listen ():
    error_count = 0
    with stt.Microphone() as source:
        try:
            audio = r.adjust_for_ambient_noise.listen(source)
            speech_out = r.recognize_google(audio)
            return speech_out
        except:
            error_count += 1


synthesis("I'm listening")

while not done:

        #check input, start options

        text = listen()

        if text != "":
            if text == "end":
                synthesis("goodbye")
                done = True
            elif text == "repeat" or "parrot":
                text = ""
                text = listen()
                print(text)
                synthesis(text)
            elif text == "calculate":
                text = ""
                text = listen()
                print(text)
                calculation = Calc.evaluate(text)
                synthesis(calculation)
        else:
            print("Nothing heard...")
