const MockData = {
    services: [
        {
            channel: "HTTP",
            chipset: "E0:D8:D8:68:B0:D8",
            mac: "9A:49:4F:54:F8:28",
            name: "Luminosidade",
            number: 3,
            numeric: 1,
            parameter: "Luminosidade local",
            unit: "%"
        },
        {
            channel: "HTTP",
            chipset: "E3:B8:Y8:J8:L0:A8",
            mac: "9E:43:4T:G4:J8:29",
            name: "Temperatura",
            number: 2,
            numeric: 1,
            parameter: "Temperatura local",
            unit: "ºC"
        },
        {
            channel: "ETHERNET",
            chipset: "I3:B4:G7:B58:L1:A9",
            mac: "9E:43:4T:G4:J8:29",
            name: "Temperatura",
            number: 1,
            numeric: 1,
            parameter: "Umidade Local",
            unit: "%"
        }
    ],
    data: [
        {
            channel: "HTTP",
            chipset: "E0:D8:D8:68:B0:D8",
            mac: "9A:49:4F:54:F8:28",
            sensitive: 0,
            serviceNumber: 3,
            time: "2020-02-08T23:07:31.715632",
            value: [ 29 ]
          },
          {
            channel: "HTTP",
            chipset: "E0:D8:D8:68:B0:D8",
            mac: "9A:49:4F:54:F8:28",
            sensitive: 0,
            serviceNumber: 3,
            time: "2020-02-08T23:07:31.715632",
            value: [ 28 ]
          },
          {
            channel: "HTTP",
            chipset: "E0:D8:D8:68:B0:D8",
            mac: "9A:49:4F:54:F8:28",
            sensitive: 0,
            serviceNumber: 3,
            time: "2020-02-08T23:07:31.715632",
            value: [ 27 ]
          }
    ],
    group: [
        { 
            group: 'Sala', 
            services: [
                {
                    channel: "HTTP",
                    chipset: "E0:D8:D8:68:B0:D8",
                    mac: "9A:49:4F:54:F8:28",
                    name: "Luminosidade",
                    number: 3,
                    numeric: 1,
                    parameter: "Luminosidade local",
                    unit: "%"
                },
                {
                    channel: "HTTP",
                    chipset: "E0:D8:D8:68:B0:D8",
                    mac: "9A:49:4F:54:F8:28",
                    name: "Temperatura",
                    number: 2,
                    numeric: 1,
                    parameter: "Temperatura Local",
                    unit: "ºC"
                },
                {
                    channel: "ETHERNET",
                    chipset: "I3:B4:G7:B58:L1:A9",
                    mac: "9E:43:4T:G4:J8:29",
                    name: "Umidade",
                    number: 3,
                    numeric: 1,
                    parameter: "Umidade Local",
                    unit: "%"
                }
            ] 
        },
    ],
    command: [
        {
            channel: "HTTP",
            chipset: "E0:D8:D8:68:B0:D8",
            mac: "9A:49:4F:54:F8:28",
            name: "Luminosidade",
            number: 3,
            numeric: 1,
            parameter: "Luminosidade local",
            unit: "%",
            command: []
        }
    ]

}
export default MockData