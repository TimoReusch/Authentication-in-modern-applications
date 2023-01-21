from manim import *


class Entities(Scene):
    def construct(self):
        font_size = 22

        client_img = ImageMobject("../assets/proton.png").scale(0.4).move_to((-5, 0.5, 0))
        client_txt = Text("Client", font_size=font_size).next_to(client_img, DOWN)

        resource_owner_img = ImageMobject("../assets/user.png").scale(0.4).move_to((-2.5, 0.5, 0))
        resource_owner_txt = Text("Resource owner", font_size=font_size).next_to(resource_owner_img, DOWN)

        resource_img = ImageMobject("../assets/memojis.png").scale(0.4).move_to((0, 0.5, 0))
        resource_txt = Text("Resource", font_size=font_size).next_to(resource_img, DOWN)

        resource_server_img = ImageMobject("../assets/google-contacts.png").scale(0.4).move_to((2.5, 0.5, 0))
        resource_server_txt = Paragraph("Resource", "server", font_size=font_size).arrange(DOWN).next_to(resource_server_img, DOWN)

        authorization_server_img = ImageMobject("../assets/google.png").scale(0.4).move_to((5, 0.5, 0))
        authorization_server_txt = Paragraph("Authorization", "server", font_size=font_size).arrange(DOWN).next_to(authorization_server_img, DOWN)

        self.add(client_txt, client_img, resource_owner_img, resource_owner_txt, resource_img, resource_txt, resource_server_img, resource_server_txt, authorization_server_img, authorization_server_txt)