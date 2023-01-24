from manim import *


class Title(Scene):
    def construct(self):
        weight = LIGHT
        title = Text("Authentifizierung in modernen Applikationen\n- ein Überblick", font="Monserrat", line_spacing=0.8, weight=weight, font_size=35, should_center=False).move_to((-2, 0, 0))
        self.play(FadeIn(title, shift=0.1*UP))
        self.wait(1)
        author = Text("Timo Reusch", font="Monserrat", weight=weight, font_size=25, should_center=False).next_to(title, DOWN*1.3, aligned_edge=LEFT)
        self.play(FadeIn(author, shift=0.1*UP))
        self.wait(1)
        self.play(FadeOut(title, author))

        headings_txt = [
            "1. HTTP Basic auth",
            "2. Cookie based authentication",
            "3. SAML 2.0 & Single Sign-On",
            "4. OAuth2 & OpenID Connect"
        ]

        counter = 0
        headings_mobjects = []
        for txt in headings_txt:
            obj = Text(txt, font="Monserrat", weight=LIGHT, font_size=33, should_center=False)
            if counter == 0:
                obj = obj.move_to((-4.5, 2.5, 0))
            else:
                obj = obj.next_to(headings_mobjects[counter-1], DOWN*2, aligned_edge=LEFT)

            counter += 1
            headings_mobjects.append(obj)

        # Show all headings once as an intro
        for obj in headings_mobjects:
            self.play(FadeIn(obj, shift=0.1*UP))
            obj.save_state()

        self.wait(1)

        for obj in headings_mobjects:
            # Create list with the objects beside the one we are presenting
            remaining_list = []
            for rem_obj in headings_mobjects:
                if rem_obj != obj:
                    remaining_list.append(rem_obj)
            # Put all Elements of the List into a VGroup
            remaining = VGroup(*remaining_list)

            self.play(obj.animate.scale(1.2).move_to((0, 0, 0)), FadeOut(remaining))
            self.wait(2)
            self.play(FadeOut(obj))
            self.wait(1)
            self.play(FadeIn(obj))
            self.play(Restore(obj), FadeIn(remaining))


class Fazit(Scene):
    def construct(self):
        weight = LIGHT
        title = Text("Fazit", font="Monserrat", line_spacing=0.8, weight=weight, font_size=35, should_center=False).move_to((0, 0, 0))
        self.play(FadeIn(title, shift=0.1*UP))
        self.wait(2)
        self.play(FadeOut(title))