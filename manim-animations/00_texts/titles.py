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
        title = Text("OpenID Connect", font="Monserrat", line_spacing=0.8, weight=weight, font_size=35, should_center=False).move_to((0, 0, 0))
        self.play(FadeIn(title, shift=0.1*UP))
        self.wait(2)
        self.play(FadeOut(title))

class Credits(Scene):
    def construct(self):
        weight = LIGHT
        title = Text("Authentifizierung in modernen Applikationen", font="Monserrat", line_spacing=0.8, weight=weight, font_size=35, should_center=False).move_to((0, 0, 0))
        subtitle = Text("- ein Überblick", font="Monserrat", line_spacing=0.8, weight=weight, font_size=35, should_center=False).next_to(title, DOWN)
        self.play(FadeIn(title, shift=0.1*UP), FadeIn(subtitle, shift=0.1*UP))
        self.wait(2)
        self.play(FadeOut(title, subtitle))
        author = Text("von Timo Reusch", font="Monserrat", line_spacing=0.8, weight=weight, font_size=35, should_center=False).move_to((0, 0, 0))
        self.play(FadeIn(author, shift=0.1*UP))
        self.wait(2)
        self.play(FadeOut(author))
        seminar2 = Text('an der Julius-Maximilians-Universität Würzburg', font="Monserrat", line_spacing=0.8, weight=weight, font_size=25).move_to((0, 0, 0))
        seminar1 = Text('Entstanden im Rahmen des Seminars "Avionic Devices"', font="Monserrat", line_spacing=0.8, weight=weight, font_size=25).next_to(seminar2, UP)
        seminar3 = Text('im Wintersemester 2022/23', font="Monserrat", line_spacing=0.8, weight=weight, font_size=25).next_to(seminar2, DOWN)
        self.play(FadeIn(seminar1, shift=0.1*UP), FadeIn(seminar2, shift=0.1*UP), FadeIn(seminar3, shift=0.1*UP))
        self.wait(3)
        self.play(FadeOut(seminar1, seminar2, seminar3))
        sources1 = Text("Quellenangaben unter:", font="Monserrat", line_spacing=0.8, weight=weight, font_size=25).move_to((0, 0, 0))
        sources2 = Text("github.com/TimoReusch/Authentication-in-modern-applications", font="Monserrat", line_spacing=0.8, weight=weight, font_size=25).next_to(sources1, DOWN)
        self.play(FadeIn(sources1, shift=0.1*UP), FadeIn(sources2, shift=0.1*UP))
        self.wait(4)
        self.play(FadeOut(sources1, sources2))
        self.wait(1)