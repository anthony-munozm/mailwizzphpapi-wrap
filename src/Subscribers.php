<?php

$app->group('/subscribers', function() use ($app){

    $app->post('/user/add', function() use ($app) {

        $endpoint = new MailWizzApi_Endpoint_ListSubscribers();

        $post = $app->request->post();
        
        if(!$post['email'] || !$post['list'] )
        {
            echo json_encode(array('status' => 'error', 'result' => 'Some parameters are missing'));
            $app->stop();
        }

        if(!isset($post['fname']))
        {
            $post['fname'] = '';
        }
        
        if(!isset($post['lname']))
        {
            $post['lname'] = '';
        }

        if(!isset($post['address']))
        {
            $post['address'] = '';
        }

        if(!isset($post['city']))
        {
            $post['city'] = '';
        }

        if(!isset($post['DSID']))
        {
            $post['DSID'] = '';
        }


        if(!isset($post['phone1']))
        {
            $post['phone1'] = '';
        }


        if(!isset($post['phone2']))
        {
            $post['phone2'] = '';
        }

        if(!isset($post['state']))
        {
            $post['state'] = '';
        }


        if(!isset($post['zip']))
        {
            $post['zip'] = '';
        }

        if(!isset($post['ip']))
        {
            $post['ip'] = '';
        }

        $response = $endpoint->createUpdate($post['list'], array(
            'EMAIL'    => $post['email'],
            'FNAME'    => $post['fname'],
            'LNAME'    => $post['lname'],
            'ADDRESS'    => $post['address'],
            'CITY'    => $post['city'],
            'DSID'    => $post['dsid'],
            'PHONE1'    => $post['phone1'],
            'PHONE2'    => $post['phone2'],
            'STATE'    => $post['state'],
            'ZIP'    => $post['zip'],
            'IP'    => $post['ip']
        ));
        echo MailWizzApi_Json::encode($response->body);
    });

    $app->post('/all', function() use ($app) {

        $endpoint = new MailWizzApi_Endpoint_ListSubscribers();
        
        $post = $app->request->post();

        $response = $endpoint->getSubscribers($post['list'], $page = 1, $perPage = 10);

        echo MailWizzApi_Json::encode($response->body);
    });

    $app->post('/user/delete', function() use ($app) {

        $endpoint = new MailWizzApi_Endpoint_ListSubscribers();
        
        $post = $app->request->post();

        $response = $endpoint->delete($post['list'], $post['subscriber_uid']);

        echo MailWizzApi_Json::encode($response->body);
    });

});
