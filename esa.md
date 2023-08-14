
<!DOCTYPE html>
<html>
<head>
<title>Web Serial Example</title>
</head>
<body>
<h1>Web Serial Example</h1>
<p>This example demonstrates how to use the Web Serial API to read and write data from two serial ports.</p>
<div id="serial-ports"></div>
<div id="form-1">
  <select id="port-1">
  </select>
  <input type="text" id="data-1" placeholder="Enter data to write to COM1">
</div>
<div id="form-2">
  <select id="port-2">
  </select>
  <input type="text" id="data-2" placeholder="Enter data to write to COM2">
</div>
<div id="rxd-1"></div>
<div id="rxd-2"></div>
<script>
const serial = navigator.serial;
const connectButton = document.getElementById("connect");
const disconnectButton = document.getElementById("disconnect");
const dataInput1 = document.getElementById("data-1");
const dataInput2 = document.getElementById("data-2");
const writeButton = document.getElementById("write");
const log = document.getElementById("log");
const rxd1 = document.getElementById("rxd-1");
const rxd2 = document.getElementById("rxd-2");

// Get a list of available serial ports.
async function getPorts() {
  const ports = await navigator.serial.getPorts();
  const availablePorts = [];
  ports.forEach((port) => {
    if (port.name !== "Unknown") {
      availablePorts.push({
        id: port.id,
        name: port.name,
      });
    }
  });
  return availablePorts;
}

// Auto populate the select a port form.
async function populatePortOptions() {
  const ports = await getPorts();
  const options = [];
  ports.forEach((port) => {
    options.push({
      value: port.id,
      text: port.name,
    });
  });
  document.getElementById("port-1").innerHTML = options;
  document.getElementById("port-2").innerHTML = options;
}

// Connect to the two serial ports selected by the user.
connectButton.addEventListener("click", async () => {
  const port1Id = document.getElementById("port-1").value;
  const port2Id = document.getElementById("port-2").value;
  const port1 = await serial.requestPort(port1Id);
  const port2 = await serial.requestPort(port2Id);
  port1.open().then(() => {
    log("Connected to port " + port1.name);
  });
  port2.open().then(() => {
    log("Connected to port " + port2.name);
  });
});

// Write data to the two serial ports selected by the user.
writeButton.addEventListener("click", async () => {
  const portId = document.getElementById("port-1").value;
  const data = dataInput1.value;
  await serial.send(portId, data);
  log("Wrote data to port " + port.name);

  const portId = document.getElementById("port-2").value;
  const data = dataInput2.value;
  await serial.send(portId, data);
  log("Wrote data to port " + port.name);
});

// Listen for events from the two serial ports selected by the user.
serial.addEventListener("connect", (event) => {
  log("Port " + event.target.name + " connected");
});
serial.addEventListener("disconnect", (event) => {
  log("Port " + event.target.name + " disconnected");
});
serial.addEventListener("data", (event) => {
  log("Received data from port " + event.target.name + ": " + event.data);
});

// Populate the select a port form on page load.
populatePortOptions();
</script>
</body>
</html>




<!DOCTYPE html>
<html>
<head>
<title>Web Serial Example</title>
</head>
<body>
<h1>Web Serial Example</h1>
<p>This example demonstrates how to use the Web Serial API to read and write data from two serial ports.</p>
<div id="serial-ports"></div>
<div id="form-1">
  <select id="port-1">
  </select>
  <input type="text" id="data-1" placeholder="Enter data to write to COM1">
</div>
<div id="form-2">
  <select id="port-2">
  </select>
  <input type="text" id="data-2" placeholder="Enter data to write to COM2">
</div>
<div id="rxd-1"></div>
<div id="rxd-2"></div>
<script>
const serial = navigator.serial;
const connectButton = document.getElementById("connect");
const disconnectButton = document.getElementById("disconnect");
const dataInput1 = document.getElementById("data-1");
const dataInput2 = document.getElementById("data-2");
const writeButton = document.getElementById("write");
const log = document.getElementById("log");
const rxd1 = document.getElementById("rxd-1");
const rxd2 = document.getElementById("rxd-2");

// Get a list of available serial ports.
async function getPorts() {
  const ports = await navigator.serial.getPorts();
  const availablePorts = [];
  ports.forEach((port) => {
    if (port.name !== "Unknown") {
      availablePorts.push({
        id: port.id,
        name: port.name,
      });
    }
  });
  return availablePorts;
}

// Auto populate the select a port form.
async function populatePortOptions() {
  const ports = await getPorts();
  const options = [];
  ports.forEach((port) => {
    options.push({
      value: port.id,
      text: port.name,
    });
  });
  document.getElementById("port-1").innerHTML = options;
  document.getElementById("port-2").innerHTML = options;
}

// Connect to the two serial ports selected by the user.
connectButton.addEventListener("click", async () => {
  const port1Id = document.getElementById("port-1").value;
  const port2Id = document.getElementById("port-2").value;
  const port1 = await serial.requestPort(port1Id);
  const port2 = await serial.requestPort(port2Id);
  port1.open().then(() => {
    log("Connected to port " + port1.name);
  });
  port2.open().then(() => {
    log("Connected to port " + port2.name);
  });
});

// Write data to the two serial ports selected by the user.
writeButton.addEventListener("click", async () => {
  const portId = document.getElementById("port-1").value;
  const data = dataInput1.value;
  await serial.send(portId, data);
  log("Wrote data to port " + port.name);

  const portId = document.getElementById("port-2").value;
  const data = dataInput2.value;
  await serial.send(portId, data);
  log("Wrote data to port " + port.name);
});

// Listen for events from the two serial ports selected by the user.
serial.addEventListener("connect", (event) => {
  log("Port " + event.target.name + " connected");
});
serial.addEventListener("disconnect", (event) => {
  log("Port " + event.target.name + " disconnected");
});
serial.addEventListener("data", (event) => {
  log("Received data from port " + event.target.name + ": " + event.data);
});

// Populate the select a port form on page load.
populatePortOptions();
</script>
</body>
</html>


<!DOCTYPE html>
<html>
<head>
<title>Web Serial Example</title>
</head>
<body>
<h1>Web Serial Example</h1>
<p>This example demonstrates how to use the Web Serial API to read and write data from two serial ports.</p>
<div id="serial-ports"></div>
<div id="form-1">
  <select id="port-1">
    <option value="">Select a port</option>
  </select>
  <input type="text" id="data-1" placeholder="Enter data to write to COM1">
</div>
<div id="form-2">
  <select id="port-2">
    <option value="">Select a port</option>
  </select>
  <input type="text" id="data-2" placeholder="Enter data to write to COM2">
</div>
<div id="rxd-1"></div>
<div id="rxd-2"></div>
<script>
const serial = navigator.serial;
const connectButton = document.getElementById("connect");
const disconnectButton = document.getElementById("disconnect");
const dataInput1 = document.getElementById("data-1");
const dataInput2 = document.getElementById("data-2");
const writeButton = document.getElementById("write");
const log = document.getElementById("log");
const rxd1 = document.getElementById("rxd-1");
const rxd2 = document.getElementById("rxd-2");

// Get a list of available serial ports.
async function getPorts() {
  const ports = await navigator.serial.getPorts();
  const availablePorts = [];
  ports.forEach((port) => {
    if (port.name !== "Unknown") {
      availablePorts.push(port);
    }
  });
  return availablePorts;
}

// Connect to the two serial ports selected by the user.
connectButton.addEventListener("click", async () => {
  const port1Id = document.getElementById("port-1").value;
  const port2Id = document.getElementById("port-2").value;
  const port1 = await getPorts().find((port) => port.id === port1Id);
  const port2 = await getPorts().find((port) => port.id === port2Id);
  port1.open().then(() => {
    log("Connected to port " + port1.name);
  });
  port2.open().then(() => {
    log("Connected to port " + port2.name);
  });
});

// Write data to the two serial ports selected by the user.
writeButton.addEventListener("click", async () => {
  const portId = document.getElementById("port-1").value;
  const data = dataInput1.value;
  await serial.send(portId, data);
  log("Wrote data to port " + port.name);

  const portId = document.getElementById("port-2").value;
  const data = dataInput2.value;
  await serial.send(portId, data);
  log("Wrote data to port " + port.name);
});

// Listen for events from the two serial ports selected by the user.
serial.addEventListener("connect", (event) => {
  log("Port " + event.target.name + " connected");
});
serial.addEventListener("disconnect", (event) => {
  log("Port " + event.target.name + " disconnected");
});
serial.addEventListener("data", (event) => {
  log("Received data from port " + event.target.name + ": " + event.data);
});
</script>
</body>
</html>



<!DOCTYPE html>
<html>
<head>
<title>Web Serial Example</title>
</head>
<body>
<h1>Web Serial Example</h1>
<p>This example demonstrates how to use the Web Serial API to read and write data from two serial ports.</p>
<div id="serial-ports"></div>
<button id="connect">Connect</button>
<button id="disconnect">Disconnect</button>
<input type="text" id="data" placeholder="Enter data to write">
<button id="write">Write</button>
<div id="log"></div>
<script>
const serial = navigator.serial;
const port1Id = "COM1";
const port2Id = "COM2";
const connectButton = document.getElementById("connect");
const disconnectButton = document.getElementById("disconnect");
const dataInput = document.getElementById("data");
const writeButton = document.getElementById("write");
const log = document.getElementById("log");

// Get a list of available serial ports.
serial.getPorts().then((ports) => {
  ports.forEach((port) => {
    const option = document.createElement("option");
    option.value = port.id;
    option.textContent = port.name;
    portList.appendChild(option);
  });
});

// Connect to the two serial ports.
connectButton.addEventListener("click", () => {
  serial.requestPort(port1Id).then((port1) => {
    serial.requestPort(port2Id).then((port2) => {
      port1.open().then(() => {
        log("Connected to port " + port1.name);
      });
      port2.open().then(() => {
        log("Connected to port " + port2.name);
      });
    });
  });
});

// Write data to the two serial ports.
writeButton.addEventListener("click", () => {
  const portId = portList.value;
  const data = dataInput.value;
  serial.send(portId, data).then(() => {
    log("Wrote data to port " + port.name);
  });
});

// Listen for events from the two serial ports.
serial.addEventListener("connect", (event) => {
  log("Port " + event.target.name + " connected");
});
serial.addEventListener("disconnect", (event) => {
  log("Port " + event.target.name + " disconnected");
});
serial.addEventListener("data", (event) => {
  log("Received data from port " + event.target.name + ": " + event.data);
});
</script>
</body>
</html>


a VEN can have multiple profiles associated to it. 

For every VEN there can be Multiple ESA's associated to it.

(VEN = OpenADR Virtual End Node, ESA = Energy Smart Appliance)

Assocaited with a profile are
 - Order
   -  The order can be MS, LD, IO or a numeric 0-999
 - Interval
   - 0-999
 - Frequency response capability
   - 0-10
- ESA IS
  - string

The profiles are identified by the Order. 

For each profile there will be a set of start times, duration and power

E.g 
start_time,duration,power
2023-02-01 11:43:18.451195+00:00,0 days 01:00:00,10000.0
2023-02-01 12:43:18.451195+00:00,0 days 01:00:00,500.0



For each ESA 1 or more profiles (identidified by Order) can be asocciated to it.
Profiles can be updated 

i.e the above data could be replaced with

start_time,duration,power
2023-02-01 11:43:18.451195+00:00,0 days 01:00:00,3000.0
2023-02-01 12:43:18.451195+00:00,0 days 03:00:00,0.0
2023-02-01 15:43:18.451195+00:00,0 days 01:00:00,10000.0
2023-02-01 16:43:18.451195+00:00,0 days 01:00:00,500.0

Note: Only the first start time is mandatory, so teh following is valid
start_time,duration,power
2023-02-01 11:43:18.451195+00:00,0 days 01:00:00,3000.0
,0 days 03:00:00,0.0
,0 days 01:00:00,10000.0
,0 days 01:00:00,500.0

This is because the other start times can be worked out from the initial start time and duration.
