# Message Broker

Message Broker is an advanced QuizXpress plugin that exchanges data with external applications and devices, such as MIDI and DMX light controllers. Use it to build effects that respond to what happens in the quiz, set up quiz rooms, control lighting, create custom game formats, or build your own external modules in environments such as [Cycling ‘74 Max](https://cycling74.com/).

This section describes QuizXpress 8.5 and later.

!!! note
    Message Broker is a licensed add-on for QuizXpress and requires a one-time purchase.

## Data channels

- **TCP/UDP:** inbound and outbound communication using plain-text messages (ASCII or UTF-8). See [IP inbound channel](ip-inbound.md) and [IP outbound channel](ip-outbound.md).
- **Telnet:** send commands and receive data directly from a Telnet console. See [IP inbound channel](ip-inbound.md).
- **MIDI:** QuizXpress events trigger configurable MIDI messages, often used to control DMX light tables. See [MIDI and DMX](midi-and-dmx.md).

This overview shows how everything is connected:

![How Message Broker connects QuizXpress to external devices](../../assets/images/mb-overview-diagram.webp){ loading=lazy }

## Opening the Message Broker settings

Message Broker is configured from QuizXpress Director while a quiz is running. Start a quiz, press the 'D' key to open [QuizXpress Director](../../live/quizxpress-director/index.md), and go to the 'Extensions' tab:

![The Extensions tab in QuizXpress Director](../../assets/images/mb-director-extensions.webp){ loading=lazy }

!!! warning
    Close the Message Broker settings with 'OK', not 'Cancel'. 'Cancel' discards all your changes.
