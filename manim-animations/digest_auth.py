from manim import *


class BasicAuthEncoding(Scene):
    def construct(self):
        ha_1_info = Text("MD5(username:realm:password)")
        ha_1_unhashed = Text("uni:Secret:wue")
        ha_1 = Text("4af6bceb84c71053b87815b8d90ae892")

        self.play(FadeIn(ha_1_info))
        self.play(ha_1_info.animate.shift(UP))
        self.play(FadeIn(ha_1_unhashed))
        self.play(Transform(ha_1_unhashed, ha_1))

        hash_1_group = VGroup().add(ha_1_info, ha_1_unhashed, ha_1)

        self.play(hash_1_group.animate.scale(0.5))
        self.play(hash_1_group.animate.shift(LEFT*4))
        self.play(hash_1_group.animate.shift(UP*2))

        ha_2_info = Text("MD5(method:digestURI)")
        ha_2_unhashed = Text("GET:secret")
        ha_2 = Text("6b3ceda96a0577176b831499e4496df6")

        self.play(FadeIn(ha_2_info))
        self.play(ha_2_info.animate.shift(UP))
        self.play(FadeIn(ha_2_unhashed))
        self.play(Transform(ha_2_unhashed, ha_2))

        hash_2_group = VGroup().add(ha_2_info, ha_2_unhashed, ha_2)

        self.play(hash_2_group.animate.scale(0.5))
        self.play(hash_2_group.animate.shift(RIGHT*4))
        self.play(hash_2_group.animate.shift(UP*2))

        ha_3_info = Text("MD5(HA1:nonce:HA2)")
        nonce = Text(": P&pMu$3#qCs :")
        ha_3 = Text("1310e12792b00f2b6a7de19049d30e37")

        self.play(FadeIn(ha_3_info))
        self.play(ha_3_info.animate.shift(UP))
        self.play(FadeIn(nonce.scale(0.5)))
        self.play(ha_1.animate.next_to(nonce, LEFT), ha_2.animate.next_to(nonce, RIGHT))
        self.wait(1)
        final_group = VGroup().add(ha_1, ha_2, nonce)
        hide_group = VGroup().add(ha_1_info, ha_2_info, hash_1_group, hash_2_group, ha_3_info)
        self.play(Transform(final_group, ha_3))

        self.wait(1)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
