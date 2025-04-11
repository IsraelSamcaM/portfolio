import reflex as rx
from portafolio.components.heading import heading
from portafolio.data import Technologylearning
from portafolio.styles.styles import EmSize, Size


def techlearning_stack(technologies: list[Technologylearning]) -> rx.Component:
    return rx.vstack(
        heading("Tecnologías en apredizaje"),
        rx.flex(
            *[
                rx.badge(
                    rx.box(
                        class_name=technology.icon,
                        font_size="24px"
                    ),
                    rx.text(technology.name),
                    size="2"
                )
                for technology in technologies
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value
    )
