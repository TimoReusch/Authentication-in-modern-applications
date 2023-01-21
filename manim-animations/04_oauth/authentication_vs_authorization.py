from manim import *


class AuthenticationVsAuthorization(Scene):
    def construct(self):
        data = ["Identify the user \nthrough something he\n • knows \n • has \n • is",
                "Is the user allowed to \ndo this?"]
        table = Table(
            [data],
            col_labels=[Text("Authentication"), Text("Authorization")]
        ).scale(0.6)

        self.play(Create(table.get_horizontal_lines()), Create(table.get_vertical_lines()))
        for i in table.get_labels():
            self.play(Write(i))
            self.wait(1)

        for i in table.get_entries_without_labels():
            self.play(FadeIn(i))
            self.wait(1)

        self.wait(1)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )