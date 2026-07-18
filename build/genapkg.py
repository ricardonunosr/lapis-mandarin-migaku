import genanki
import yaml
import sys

if len(sys.argv) < 2:
    print("Usage: python genapkg.py <output_file>")
    sys.exit(1)

LAPIS_MANDARIN_MIGAKU_TEMPLATE_ID = 1667218449924
LAPIS_MANDARIN_MIGAKU_DECK_ID = 1759068131724

with open("../src/front.html", "r", encoding="utf-8") as front_file:
    front_content = front_file.read()

with open("../src/back.html", "r", encoding="utf-8") as back_file:
    back_content = back_file.read()

with open("../src/styling.css", "r", encoding="utf-8") as css_file:
    css_content = css_file.read()

with open("anki_fields.yaml", "r", encoding="utf-8") as fields_file:
    anki_fields = yaml.safe_load(fields_file)

lapis = genanki.Model(
    LAPIS_MANDARIN_MIGAKU_TEMPLATE_ID,
    "Lapis Mandarin Migaku",
    fields=anki_fields,
    templates=[
        {
            "name": "Mining",
            "qfmt": front_content,
            "afmt": back_content,
        },
    ],
    css=css_content,
)

deck = genanki.Deck(LAPIS_MANDARIN_MIGAKU_DECK_ID, "Lapis Mandarin Migaku")

with open("example_card.csv", "r", encoding="utf-8") as f:
    for line in f:
        fields_content = line.strip().split("\t")
        deck.add_note(
            genanki.Note(
                model=lapis, fields=fields_content, tags=["the_last_of_us"]
            )
        )

package = genanki.Package(deck)
package.media_files = [
    "media_files/b1190ef3ec7.mp3",
    "media_files/7bc68b1190e.mp3",
    "media_files/d8ecd7bc68b.webp",
]
package.write_to_file(sys.argv[1])
