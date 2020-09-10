package main

import (
	"log"

	"github.com/gofiber/fiber"
	"github.com/stianeikeland/go-rpio/v4"
)

func main() {
	app := fiber.New()

	type LightEvent struct {
		EventType string `json:"event_type"`
		Gpio      int    `json:"gpio"`
	}

	type EventResponse struct {
		Status   string `json:"status"`
		PinState string `json:"pin_state"`
	}

	app.Get("/", func(c *fiber.Ctx) {
		c.Send("Hello, World 👋!")
	})

	app.Post("/", func(c *fiber.Ctx) {
		le := new(LightEvent)
		if err := c.BodyParser(le); err != nil {
			log.Fatal(err)
		}

		_ = rpio.Open()
		// 10,7,6
		pin := rpio.Pin(le.Gpio)

		pin.Output()

		log.Println(le.EventType) // john
		if le.EventType == "toggle" {
			pin.Toggle()
		}
		if le.EventType == "on" {
			pin.High()
		}
		if le.EventType == "off" {
			pin.Low()
		}

		// pin.Input() // Input mode
		// res := pin.Read() // Read state from pin (High / Low)
		evr := EventResponse{
			Status:   "ok",
			PinState: le.EventType,
		}
		c.JSON(evr)
	})

	app.Listen(3000)
}
