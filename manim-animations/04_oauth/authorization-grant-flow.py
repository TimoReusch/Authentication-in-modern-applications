from manim import *


class AuthorizationGrantFlow(Scene):
    def construct(self):
        font_size = 22

        resource_owner_img = ImageMobject("../assets/user.png").scale(0.4).move_to((-5, 0.5, 0))
        resource_owner_txt = Text("Resource owner", font_size=font_size).next_to(resource_owner_img, DOWN)

        client_img = ImageMobject("../assets/proton.png").scale(0.4).move_to((-2.5, 0.5, 0))
        client_txt = Text("Client", font_size=font_size).next_to(client_img, DOWN)

        resource_img = ImageMobject("../assets/memojis.png").scale(0.4).move_to((0, 0.5, 0))
        resource_txt = Text("Resource", font_size=font_size).next_to(resource_img, DOWN)

        authorization_server_img = ImageMobject("../assets/google.png").scale(0.4).move_to((2.5, 0.5, 0))
        authorization_server_txt = Paragraph("Authorization", "server", font_size=font_size).arrange(DOWN).next_to(authorization_server_img, DOWN)

        resource_server_img = ImageMobject("../assets/google-contacts.png").scale(0.4).move_to((5, 0.5, 0))
        resource_server_txt = Paragraph("Resource", "server", font_size=font_size).arrange(DOWN).next_to(resource_server_img, DOWN)

        self.play(FadeIn(client_img), FadeIn(resource_owner_img), FadeIn(resource_img), FadeIn(resource_server_img), FadeIn(authorization_server_img))
        self.wait(1)
        self.play(Write(resource_txt))
        self.wait(1)
        self.play(Write(resource_owner_txt))
        self.wait(1)
        self.play(Write(resource_server_txt))
        self.wait(1)
        self.play(Write(authorization_server_txt))
        self.wait(1)
        self.play(Write(client_txt))
        self.wait(1)

        # Config
        tip = 0.2
        font_size = 22

        x_browser = -6
        x_client = -2.5
        x_auth = 1
        x_login = 3.5
        x_res = 6
        x_mid_browser_client = -4.25

        y_first = 2.2
        y_arrow_space = 0.75
        y_text_space = 0.2

        # Sequence Diagram Base
        browser_line = DashedLine((x_browser, 2.7, 0), (x_browser, -3.5, 0)).set_z_index(-5)
        browser_img = ImageMobject("../assets/firefox.png").scale(0.2).next_to(browser_line, UP).set_z_index(-5)

        client_line = DashedLine((x_client, 2.7, 0), (x_client, -3.5, 0)).set_z_index(-5)

        auth_server_line = DashedLine((x_auth, 2.7, 0), (x_auth, -3.5, 0)).set_z_index(-5)

        resource_server_line = DashedLine((x_res, 2.7, 0), (x_res, -3.5, 0)).set_z_index(-5)

        self.play(FadeOut(resource_owner_txt),
                  FadeOut(client_txt),
                  FadeOut(resource_txt),
                  FadeOut(authorization_server_txt),
                  FadeOut(resource_txt),
                  FadeOut(resource_server_txt))

        self.play(FadeIn(browser_img),
                  client_img.animate.scale(0.5).next_to(client_line, UP),
                  authorization_server_img.animate.scale(0.5).next_to(auth_server_line, UP),
                  resource_server_img.animate.scale(0.5).next_to(resource_server_line, UP),
                  resource_owner_img.animate.set_z_index(-4).scale(0.5).move_to((x_browser-0.5, 3.2, 0)),
                  FadeOut(resource_img))

        self.play(Create(browser_line),
                  Create(client_line),
                  Create(auth_server_line),
                  Create(resource_server_line))
        self.wait(1)

        # --------------------------------------------------------------------------------------------------------------
        # Arrow: Browser -> Proton
        y_a1 = y_first
        request_contacts_arrow = Line((x_browser, y_a1, 0), (x_client, y_a1, 0))\
            .add_tip(tip_width=tip, tip_length=tip).set_z_index(-4)
        request_contacts_arrow_txt = Text("Request contact import", font_size=font_size)\
            .move_to((-4.24, y_a1+y_text_space, 0)).set_z_index(-4)
        self.play(Create(request_contacts_arrow), FadeIn(request_contacts_arrow_txt))
        self.wait(1)

        # Arrow: Proton -> Google
        y_a2 = y_a1 - y_arrow_space
        r_1 = Line((x_client, 2, 0), (-5.9, 2, 0)).set_z_index(-4)
        r_2 = Line((-5.9, 2, 0), (-5.9, y_a2, 0)).set_z_index(-4)
        r_3 = Line((-5.9, y_a2, 0), (x_auth, y_a2, 0)).add_tip(tip_width=tip, tip_length=tip).set_z_index(-4)
        resource_owner_img.set_z_index(-3)
        redirect_to_google = VGroup().add(r_1, r_2)
        redirect_to_google.set_z_index(-4)
        redirect_txt = Text("Authorization Request", font_size=font_size).move_to((x_mid_browser_client, y_a2+y_text_space, 0)).set_z_index(-4)
        self.play(Create(redirect_to_google), resource_owner_img.animate.next_to(r_3, LEFT*0.1))

        # --- Login-Section ---
        arrow_google_login = Line((x_auth, 1.45, 0), (2, 2.15, 0)).add_tip(tip_width=tip, tip_length=tip)
        login = ImageMobject("../assets/google-sign-in.png").move_to((x_login, 2.15, 0)).scale(0.33).set_z_index(-4)
        self.play(Create(r_3),
                  FadeIn(redirect_txt),
                  Create(arrow_google_login),
                  FadeIn(login),
                  resource_owner_img.animate.move_to((2, 2.7, 0)))
        self.wait(1)

        arrow_login_consent = Line((x_login, 1.2, 0), (x_login, 0.3, 0)).add_tip(tip_width=tip, tip_length=tip)
        consent = ImageMobject("../assets/consent.png").scale(0.29).move_to((x_login, 0, 0)).set_z_index(-4)
        self.play(Create(arrow_login_consent), FadeIn(consent), resource_owner_img.animate.move_to((2, 0, 0)))
        self.wait(1)

        arrow_consent_google = Line((2, 0, 0), (x_auth, y_a2-y_arrow_space, 0)).add_tip(tip_width=tip, tip_length=tip)
        # ---------------------

        # Arrow: Google -> Firefox
        y_a3 = y_a2 - y_arrow_space
        authorization_code = DashedLine((1, y_a3, 0), (-6, y_a3, 0)).add_tip(tip_width=tip, tip_length=tip).set_z_index(-4)
        code = Text("Authorization code (/callback)", font_size=font_size).move_to((x_client, y_a3+y_text_space, 0)).set_z_index(-4)
        self.play(Create(arrow_consent_google),
                  Create(authorization_code),
                  FadeIn(code),
                  resource_owner_img.animate.move_to((x_browser-0.5, 3.2, 0)))
        self.wait(1)

        # Arrow: Browser -> Proton
        y_a4 = y_a3 - y_arrow_space
        code_to_backend = Line((x_browser, y_a4, 0), (x_client, y_a4, 0)).add_tip(tip_width=tip, tip_length=tip)
        code_to_backend_txt = Text("Authorization code", font_size=font_size).move_to((-4.24, y_a4+y_text_space, 0))
        self.play(Create(code_to_backend), FadeIn(code_to_backend_txt))
        self.wait(1)

        # Arrow: Proton -> Google
        y_a5 = y_a4 - y_arrow_space
        code_client_auth = Line((x_client, y_a5, 0), (x_auth, y_a5, 0)).add_tip(tip_width=tip, tip_length=tip)
        code_client_auth_txt = Text("Code + secret (/token)", font_size=font_size).move_to((-0.7, y_a5+y_text_space, 0))
        self.play(Create(code_client_auth), FadeIn(code_client_auth_txt))
        self.wait(1)

        # Arrow: Google -> Proton
        y_a6 = y_a5 - 0.5
        token_auth_client = DashedLine((x_auth, y_a6, 0), (x_client, y_a6, 0)).add_tip(tip_width=tip, tip_length=tip)
        token_auth_client_txt = Text("Token", font_size=font_size).move_to((-0.7, y_a6+y_text_space, 0))

        access_token_code = '''
{
  "access_token": "aEHcyKhkL6FLSWJwiYoD3dMRN2e4bY",
  "expires_in": 3920,
  "token_type": "Bearer"
}
'''
        rendered_code_access_token = Code(code=access_token_code, tab_width=2, background="rectangle", insert_line_no=False, style="github-dark",
                             line_spacing=0.8, language="json", font="Monospace", background_stroke_width=0).scale(0.3).move_to((-4.25, y_a6, 0))
        rendered_code_access_token[0].set_z_index(-2)
        self.play(Create(token_auth_client), FadeIn(token_auth_client_txt), FadeIn(rendered_code_access_token))
        self.wait(1)

        # Arrow: Proton -> Google Contacts
        y_a7 = y_a6 - y_arrow_space
        token_client_contact = Line((x_client, y_a7, 0), (x_res, y_a7, 0)).add_tip(tip_width=tip, tip_length=tip)

        get_contacts_code = '''
GET people.googleapis.com
Authorization: Bearer aEHcyKhkL6FLSWJwiYoD3dMRN2e4bY        
'''
        rendered_code_get_contacts = Code(code=get_contacts_code,
                                          tab_width=2,
                                          background="rectangle",
                                          insert_line_no=False,
                                          style="github-dark",
                                          line_spacing=0.8,
                                          language="python",
                                          font="Monospace",
                                          background_stroke_width=0)\
            .scale(0.4).move_to((2, y_a7+0.4, 0))
        rendered_code_get_contacts[0].set_z_index(-2)

        self.play(Create(token_client_contact), FadeIn(rendered_code_get_contacts))
        self.wait(1)

        highlight = BackgroundRectangle(rendered_code_get_contacts[2][1],
                                        stroke_width=1,
                                        buff=0.05,
                                        color=GREEN,
                                        fill_opacity=0.5, z_index=-1)
        self.play(Create(highlight))

        self.wait(1)

        self.play(FadeOut(highlight))

        # Arrow: Google Contacts -> Proton
        y_a8 = y_a7 - 0.5
        contacts_res_client = DashedLine((x_res, y_a8, 0), (x_client, y_a8, 0)).add_tip(tip_width=tip, tip_length=tip)
        contacts_res_client_txt = Text("Contacts", font_size=font_size).move_to((2, y_a8+y_text_space, 0))
        # resource_img.scale(0.7).move_to((2, y_a8-0.6, 0))
        self.play(Create(contacts_res_client), FadeIn(contacts_res_client_txt))
        self.wait(1)

        # Arrow: Proton -> Browser
        y_a9 = y_a8 - 0.5
        contacts_res_client = DashedLine((x_client, y_a9, 0), (x_browser, y_a9, 0)).add_tip(tip_width=tip, tip_length=tip)
        contacts_res_client_txt = Text("Success!", font_size=font_size).move_to((-4.25, y_a9+y_text_space, 0))
        self.play(Create(contacts_res_client), FadeIn(contacts_res_client_txt))
        self.wait(1)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )