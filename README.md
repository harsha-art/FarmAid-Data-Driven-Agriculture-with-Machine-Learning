# Agriculture-Portal-Flood-Prediction

Agriculture Portal is a machine learning-based platform for farmers. The system uses advanced algorithms to provide recommendations for fertilizers and crops while providing accurate rainfall, crop and yield predictions to help farmers make informed data-driven decisions about their crops.
Our platform utilizes Decision Trees (with Gini Impurity) and the Random Forest Machine Learning Model to ensure optimal accuracy. These models have been meticulously trained and tested in research to provide reliable predictions and recommendations. 

We also use the weather data to predict flood using an IOT device equipped with an ultrasound sensor. This feature aims to provide farmers with alerts, helping them safeguard their crops and mitigate potential losses due to flooding.

# Installation
1. Clone the repository to your local machine.
```
git clone https://github.com/harsha-art/FarmAid-Data-Driven-Agriculture-with-Machine-Learning.git
```

2. Goto Farmers folder and Install the required packages using pip.
```
pip install -r requirements.txt
```

3. Change Success Url and Cancel Url file paths in customer/cbuy_crops.php.
```
$session = \Stripe\Checkout\Session::create([
'payment_method_types' => ['card'],
	'line_items' => [[
	'price_data' => [
		'product' => 'prod_NdAYaoDLX3DnMY',
		'unit_amount' => $TotalCartPrice,
		'currency' => 'inr',
		],
		'quantity' => 1,
		]],
	'mode' => 'payment',
	'success_url' => 'http://localhost/projects/agri2/customer/cupdatedb.php',   // Change File Path
	'cancel_url' => 'http://localhost/projects/agri2/customer/cbuy_crops.php',   // Change File Path
]);
```
4. Add API Keys to respective files.
- News API Key to fnewsfeed.php
- OpenWeatherMap API Key to fweather_forecast.php
- Stripe API Key to customer/stripePayment/config.php
- OpenAI API Key to index.php and fchatgpt.php

5. Import database from db folder.
6. Run Apache web server using XAMPP.
