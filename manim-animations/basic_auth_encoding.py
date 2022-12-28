from manim import *


class BasicAuthEncoding(Scene):
    def construct(self):
        credentials = Text("Username: uni\nPassword: wue")

        self.play(FadeIn(credentials))
        self.wait(1)

        self.play(credentials.animate.shift(UP))
        self.play(credentials.animate.scale(0.5))

        user_pass = Text("uni:wue")
        self.play(FadeIn(user_pass))
        self.wait(1)

        user_pass_encoded = Text("dW5pOnd1ZQ==")

        self.play(Transform(user_pass, user_pass_encoded))

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
