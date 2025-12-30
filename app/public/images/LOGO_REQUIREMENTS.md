# Logo Requirements for Bible Trivia App

## Image Specifications
- **Format**: PNG with transparency
- **Dimensions**: 700×700 pixels (square)
- **Design**: Circular medallion style
- **Total Images**: 24 (12 themes × 2 variants)

## Required Logo Files

### Logos Folder (With Text)
Place these files in: `app/public/images/Logos/`
- `miracles.png`
- `prophets.png`
- `apostles.png`
- `kings-rulers.png`
- `women-of-faith.png`
- `battles-conquests.png`
- `parables-teachings.png`
- `creation-origins.png`
- `prophecy-end-times.png`
- `journeys-exile.png`
- `festivals-customs.png`
- `wisdom-psalms.png`

### LogosNoText Folder (Without Text)
Place these files in: `app/public/images/LogosNoText/`
- `miraclesnotext.png`
- `prophetsnotext.png`
- `apostlesnotext.png`
- `kings-rulersnotext.png`
- `women-of-faithnotext.png`
- `battles-conquestsnotext.png`
- `parables-teachingsnotext.png`
- `creation-originsnotext.png`
- `prophecy-end-timesnotext.png`
- `journeys-exilenotext.png`
- `festivals-customsnotext.png`
- `wisdom-psalmsnotext.png`

## Theme Name Mapping

| Display Name | File Name Base | Theme Code |
|--------------|----------------|------------|
| Miracles | miracles | MIR |
| Prophets | prophets | PRO |
| Apostles | apostles | APO |
| Kings & Rulers | kings-rulers | KIN |
| Women of Faith | women-of-faith | WOM |
| Battles & Conquests | battles-conquests | BAT |
| Parables & Teachings | parables-teachings | PAR |
| Creation & Origins | creation-origins | CRE |
| Prophecy & End Times | prophecy-end-times | PRE |
| Journeys & Exile | journeys-exile | JOU |
| Festivals & Customs | festivals-customs | FES |
| Wisdom & Psalms | wisdom-psalms | WIS |

## Usage Context

### Logos (with text)
- **Where**: Theme selection screen
- **Purpose**: Help users identify and select quiz themes
- **Display Size**: ~120px in theme selector cards

### LogosNoText (without text)
- **Where**: During quiz gameplay
- **Purpose**: Visual theme identifier for each question
- **Display Size**: ~60-80px in question header badge

## Implementation Notes
- Images will be loaded dynamically based on theme name
- Fallback to text-only display if image fails to load
- Images should be optimized for web delivery
- Consider implementing lazy loading for performance
