from manim import *


class BasicAuth(Scene):
    def construct(self):
        left_x = -4
        right_x = 4
        font_size_big = 30
        font_size_small = 22
        tip = 0.2

        # Client side
        client = Text(text="Client", font_size=font_size_big)
        line_c = DashedLine((left_x, -3, 0), (left_x, 3, 0))
        client.next_to(line_c, UP)
        self.add(line_c, client)

        # Server side
        server = Text(text="Server", font_size=font_size_big)
        line_s = DashedLine((right_x, -3, 0), (right_x, 3, 0))
        server.next_to(line_s, UP)
        self.add(line_s, server)



        # GET /secretPage
        arrow_progress_1 = Line((left_x, 2, 0), (right_x, 2, 0)).add_tip(tip_width=tip, tip_length=tip)
        description_for_1 = Text(text="GET /secretPage", font_size=font_size_small)
        description_for_1.next_to(arrow_progress_1, UP/5)
        self.add(arrow_progress_1, description_for_1)

        # Response WWW-Authenticate
        arrow_progress_2 = DashedLine((right_x, 1, 0), (left_x, 1, 0)).add_tip(tip_width=tip, tip_length=tip)
        description_for_2 = Text(text='401 Unauthorized\nWWW-Authenticate: Basic realm="Secret"',
                                 font_size=font_size_small)
        description_for_2.next_to(arrow_progress_2, UP/5)
        self.add(arrow_progress_2, description_for_2)

        # Client gets credentials
        c1 = Line((left_x, 0.5, 0), (left_x-0.5, 0.5, 0))
        c2 = Line((left_x-0.5, 0.5, 0), (left_x-0.5, 0, 0))
        c3 = Line((left_x-0.5, 0, 0), (left_x, 0, 0)).add_tip(tip_width=tip, tip_length=tip)
        arrow_progress_3 = VGroup().add(c1, c2, c3)
        description_for_3 = Text(text="Obtain\ncredentials", font_size=font_size_small)
        description_for_3.next_to(arrow_progress_3, LEFT)
        self.add(arrow_progress_3, description_for_3)

        # Client sends encoded credentials
        arrow_progress_4 = Line((left_x, -0.5, 0), (right_x, -0.5, 0)).add_tip(tip_width=tip, tip_length=tip)
        description_for_4 = Text(text="GET /secretPage\nAuthorization: Basic dW5pOnd1ZQ==", font_size=font_size_small)
        description_for_4.next_to(arrow_progress_4, UP/5)
        self.add(arrow_progress_4, description_for_4)

        # Server validates credentials
        s1 = Line((right_x, -1, 0), (right_x+0.5, -1, 0))
        s2 = Line((right_x+0.5, -1, 0), (right_x+0.5, -1.5, 0))
        s3 = Line((right_x+0.5, -1.5, 0), (right_x, -1.5, 0)).add_tip(tip_width=tip, tip_length=tip)
        arrow_progress_5 = VGroup().add(s1, s2, s3)
        description_for_5 = Text(text="Validate\ncredentials", font_size=font_size_small)
        description_for_5.next_to(arrow_progress_5, RIGHT)
        self.add(arrow_progress_5, description_for_5)

        # Servers response to credentials
        arrow_progress_6 = DashedLine((right_x, -2, 0), (left_x, -2, 0)).add_tip(tip_width=tip, tip_length=tip)
        description_for_6 = Text(text="200 OK or 401 Unauthorized",
                                 font_size=font_size_small)
        description_for_6.next_to(arrow_progress_6, UP/5)
        self.add(arrow_progress_6, description_for_6)
