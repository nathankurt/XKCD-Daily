![XKCD DAILY COMIC](https://github.com/nathankurt/XKCD-Daily/workflows/XKCD%20DAILY%20COMIC/badge.svg)

# XKCD-Daily
I really love the XKCD Comics and wanted to play around with Twilio so I decided to make a bot to scrape some data with it. 

Because I'm too lazy to actually go and check the XKCD website, I created a bot using Python and the Twilio API to send a text message that contains:
  * Latest XKCD Comic Image
  * The Comic Number
  * The Title
  * The Alt Text

![XKCD Comic Text](https://user-images.githubusercontent.com/9864281/75191785-06edb380-5721-11ea-8069-53a1c3dd7786.jpg)


## Create Yourself

If you want to do something similar, this works with a Twilio Trial Account. Fork this repo and make a Twilio Account. After you make the account go ahead and grab the following
  * A phone number with MMS support. - `TWILIO_PHONE_NUMBER`
  * Twilio Account SID - `TWILIO_ACCOUNT_SID`
  * Twilio Auth Token - `TWILIO_AUTH_TOKEN`
  * A Verified Number to send to. - `TO_PHONE_NUMBER`

Take those things and make them secrets in GitHub Settings and name them the name I have associated above. As long as your phone number is verified, the action should run and send a text.
If it's a trial account, it will contain a line that says `Sent from your Twilio Trial Account` which is a little annoying, but can be avoided if you decide to upgrade your account. 

![XKCD Comic Text](https://user-images.githubusercontent.com/9864281/75191785-06edb380-5721-11ea-8069-53a1c3dd7786.jpg)

# References
All comic and image credit goes to [XKCD](https://xkcd.com) 