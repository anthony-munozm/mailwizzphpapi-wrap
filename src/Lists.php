<?php

$app->group('/lists', function() use ($app) {
    $app->post('/get', function() use ($app) {
        $endpoint = new MailWizzApi_Endpoint_Lists();
        if(!$app->request()->post('list'))
        {
            echo json_encode(array('status' => 'error', 'result' => 'Parameter [list] is missing'));
            $app->stop();
        }
        $response = $endpoint->getList($app->request()->get('list'));
        echo MailWizzApi_Json::encode($response->body);
    });

    $app->get('/show', function() use ($app) {

        $endpoint = new MailWizzApi_Endpoint_Lists();
        $response = $endpoint->getLists();
        echo MailWizzApi_Json::encode($response->body);
    });

    $app->post('/fields', function() use ($app) {

        $endpoint = new MailWizzApi_Endpoint_ListFields();
        if(!$app->request()->post('list'))
        {
            echo json_encode(array('status' => 'error', 'result' => 'Parameter [list] is missing'));
            $app->stop();
        }
        $response = $endpoint->getFields($app->request()->get('list'));
        echo MailWizzApi_Json::encode($response->body);
    });

    $app->post('/segments', function() use ($app) {

        $endpoint = new MailWizzApi_Endpoint_ListSegments();
        if(!$app->request()->post('list'))
        {
            echo json_encode(array('status' => 'error', 'result' => 'Parameter [list] is missing'));
            $app->stop();
        }
        $response = $endpoint->getSegments($app->request()->post('list'));
        echo MailWizzApi_Json::encode($response->body);
    });

    $app->post('/create', function() use ($app) {

        $endpoint = new MailWizzApi_Endpoint_Lists();

        $post = $app->request->post();

        if(!isset($post['general_name']))
        {
            $post['general_name'] = 'Subscribers';
        }
        if(!isset($post['general_description']))
        {
            $post['general_description'] = 'This is a Subscribers list, created from the API.';
        }
        if(!isset($post['defaults_from_name']))
        {
            $post['defaults_from_name'] = 'John Doe';
        }
        if(!isset($post['defaults_from_email']))
        {
            $post['defaults_from_email'] = 'johndoe@doe.com';
        }
        if(!isset($post['defaults_reply_to']))
        {
            $post['defaults_reply_to'] = 'johndoe@doe.com';
        }
        if(!isset($post['defaults_subject']))
        {
            $post['defaults_subject'] = 'Subscribers';
        }
        if(!isset($post['notifications_subscribe']))
        {
            $post['notifications_subscribe'] = 'yes';
        }
        if(!isset($post['notifications_unsubscribe']))
        {
            $post['notifications_unsubscribe'] = 'yes';
        }
        if(!isset($post['notifications_subscribe_to']))
        {
            $post['notifications_subscribe_to'] = 'johndoe@doe.com';
        }
        if(!isset($post['notifications_unsubscribe_to']))
        {
            $post['notifications_unsubscribe_to'] = 'johndoe@doe.com';
        }
        if(!isset($post['company_name']))
        {
            $post['company_name'] = 'John Doe INC';
        }
        if(!isset($post['company_country']))
        {
            $post['company_country'] = 'United States';
        }
        if(!isset($post['company_zone']))
        {
            $post['company_zone'] = 'New York';
        }
        if(!isset($post['company_address_1']))
        {
            $post['company_address_1'] = 'Some street address';
        }
        if(!isset($post['company_address_2']))
        {
            $post['company_address_2'] = '';
        }
        if(!isset($post['company_zone_name']))
        {
            $post['company_zone_name'] = '';
        }
        if(!isset($post['company_city']))
        {
            $post['company_city'] = 'New York City';
        }
        if(!isset($post['company_zip_code']))
        {
            $post['company_zip_code'] = '10019';
        }

        $response = $endpoint->create(array(
            // required
            'general' => array(
                'name'          => $post['general_name'], // required
                'description'   => $post['general_description'], // required
            ),
            // required
            'defaults' => array(
                'from_name' => $post['defaults_from_name'], // required
                'from_email'=> $post['defaults_from_email'], // required
                'reply_to'  => $post['defaults_reply_to'], // required
                'subject'   => $post['defaults_subject'],
            ),
            // optional
            'notifications' => array(
                // notification when new subscriber added
                'subscribe'         => $post['notifications_subscribe'], // yes|no
                // notification when subscriber unsubscribes
                'unsubscribe'       => $post['notifications_unsubscribe'], // yes|no
                // where to send the notifications.
                'subscribe_to'      => $post['notifications_subscribe_to'],
                'unsubscribe_to'    => $post['notifications_unsubscribe_to'],
            ),
            // optional, if not set customer company data will be used
            'company' => array(
                'name'      => $post['company_name'], // required
                'country'   => $post['company_country'], // required
                'zone'      => $post['company_zone'], // required
                'address_1' => $post['company_address_1'], // required
                'address_2' => $post['company_address_2'],
                'zone_name' => $post['company_zone_name'], // when country doesn't have required zone.
                'city'      => $post['company_city'],
                'zip_code'  => $post['company_zip_code'],
            ),
        ));
        // and get the response
        print_r($response->body);
        echo MailWizzApi_Json::encode($response->body);
    });

});