*This post is one of a series of articles adapted from my university dissertation on data
visualisation — see the [rest of the series](/blog/tags/datavis-project).*

I undertook a challenge to hack (not in the illegal, immoral meaning of the word) some public
transport data and find a way of making it useful. I chose the motorway matrix display boards in
Sheffield — the boards that display a message relaying current traffic information such as:

"Football match at Hillsborough 15:00 expect delays"; "Slow — 40 — accident"; "Junction 32 closed".

There is a website which allows members of the public to connect to a live stream of these board
displays. The only problem is they are in raw format, and require serious programming reformatting
wizardry and RegEx magic. I was learning Ruby at the time so I decided to use this to attempt the
task.

The website is `backend.yorkshirevoyager.com` and this particular resource is located at:

```
/voyager_webservices/WebServices.asmx/VMS_GetReviewNetworks
```

```
# Gets the VMS data, outputs it nicely formatted.
require 'net/http'
require 'uri'
require 'rexml/document'

vms_data_url = 'http://backend.yorkshirevoyager.com/voyager_webservices/WebServices.asmx/VMS_GetReviewNetworks'
vms_data_xml = Net::HTTP::post_form(URI.parse(vms_data_url), {}).body
vms_data_doc = REXML::Document.new(vms_data_xml)

messages = []
delimiters = []
xs = []
ys = []

vms_data_doc.elements.each('getVMS/reviewVMS/Message') do |element|
  messages << element.text
end

vms_data_doc.elements.each('getVMS/reviewVMS/Delimiter') do |element|
  delimiters << element.text
end

vms_data_doc.elements.each('getVMS/reviewVMS/x') do |element|
  xs << element.text
end

vms_data_doc.elements.each('getVMS/reviewVMS/y') do |element|
  ys << element.text
end

formatted_messages = []
messages.each_with_index do |message, index|
  puts "x: #{xs[index]}, y: #{ys[index]}, message: #{message.gsub(/[\s]*\|[\s]*/, ", ").gsub(/,[\s]*,/, "").gsub(/[\s]+/, " ").gsub(/[\s]*,[\s]*$/, "").gsub(/^[\s]*,[\s]*/, "")}\n\n" if message.length > 7
end
```

This Ruby file performed an HTTP POST request and sent the data to arrays containing the x-y
coordinates of the location of the message boards, and the actual full text of the message — which
were horrifically structured due to spacing issues and bad use of delimiters. The RegEx ensures all
unnecessary (padding) white spaces and delimiters were eradicated, and that blank messages were
ignored. The terminal output looked like this:

```
x: 457580, y: 396982, message: TO J41 (FOR M62), 17 MILES, 15 MINS
x: 455441, y: 399901, message: TO GRANTHAM, 49 MILES, 45 MINS
x: 438473.71875, y: 386973.4375, message: TO M1 J33, 5 MINUTES
x: 433607.71875, y: 391570.78125, message: FOOTBALL MATCH, HILLSBOROUGH, SAT 02-04-11, 15:00
x: 434414.75, y: 386866.9375, message: FOOTBALL MATCH, HILLSBOROUGH, SAT 02-04-11, 15:00
```

The x and y coordinates are OS (Ordnance Survey) map coordinates.

I then adapted the program to output to CSV:

```
File.open('output.csv','w') do |f|
  formatted_messages.each do |message|
    f.puts message
  end
end
```

This sent all the data to a CSV file like so:

```
457981,396350,"M18 CLOSED, J2-J1"
457580,396982,"M18 CLOSED, J2-J1"
455441,399901,"M18 CLOSED, J2-J1"
454965,400344,"M18 CLOSED, J2-J1"
438473.71875,386973.4375,"TO M1 J33, 5 MINUTES"
433607.71875,391570.78125,"FOOTBALL MATCH, HILLSBOROUGH, SAT 02-04-11, 15:00"
434414.75,386866.9375,"FOOTBALL MATCH, HILLSBOROUGH, SAT 02-04-11, 15:00"
```

Now with x-y coordinates and messages properly formatted, this data can be sent to another source such
as Google Maps or Open Street Maps API. It is a difficult mathematical task to convert x-y coordinates
to longitude/latitude due to having to take into account the curvature of the Earth, but there are PHP
scripts and such available to do so.
