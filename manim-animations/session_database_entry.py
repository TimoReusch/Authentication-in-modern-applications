from manim import *


class SessionDatabaseEntry(Scene):
    def construct(self):
        data = ["730",
                "2023-01-01 01:25:03",
                "241.40.79.64",
                "Mozilla/5.0 (Macintosh;\n Intel Mac OS X 10_15_7)\n"
                "AppleWebKit/537.36\n (KHTML, like Gecko)\n"
                "Chrome/108.0.0.0\n"
                "Safari/537.36",
                "bHExmo2AXLgiC87hw\nNQEdqNEo2JjWU"]
        table = Table(
            [data],
            col_labels=[Text("userId"), Text("loginTime"), Text("ipAddress"), Text("userAgent"), Text("sessionId")]) \
            .scale(0.4)
        self.play(table.create(label_animation=FadeIn, element_animation=Write))
        self.wait(1)
        self.play(FadeIn(table.get_cell((2, 5)).set_fill(GREEN, 0.3).set_stroke(GREEN)))
        self.wait(1)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
