

def sub(project_id, subscription_name):
    import time
    # [START pubsub_quickstart_sub_deps]
    from google.cloud import pubsub_v1,pubsub
    """Receives messages from a Pub/Sub subscription."""
    # [START pubsub_quickstart_sub_client]
    # Initialize a Subscriber client
    client = pubsub_v1.SubscriberClient()
    # [END pubsub_quickstart_sub_client]
    # Create a fully qualified identifier in the form of
    # `projects/{project_id}/subscriptions/{subscription_name}`
    subscription_path = client.subscription_path(
        project_id, subscription_name)

    def callback(message):
        print('Received message {} of message ID {}'.format(
            message, message.message_id))
        # Acknowledge the message. Unack'ed messages will be redelivered.
        message.ack()
        print('Acknowledged message of message ID {}\n'.format(
            message.message_id))

    client.subscribe(subscription_path, callback=callback)
    print('Listening for messages on {}..\n'.format(subscription_path))

    # Keep the main thread from exiting so the subscriber can
    # process messages in the background.
    while True:
        time.sleep(60)

def createSuscription():
    publisherClient = pubsub_v1.PublisherClient()
    suscriberClient = pubsub_v1.SubscriberClient()
    

def create_topic(project_id, topic_name):
    from google.cloud import pubsub_v1, pubsub
    publisher = pubsub.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    try:
        topic = publisher.create_topic(topic_path)
        print('Topic created: {}'.format(topic))
    except Exception as e:
        print("Oucrrio un problema")
        print(e)

# create_topic("buho-platform","myTopic")


def publish_messages(project_id, topic_name):
    """Publishes multiple messages to a Pub/Sub topic."""
    from google.cloud import pubsub_v1
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    for n in range(1, 10):
        data = u'Message number {}'.format(n)
        data = data.encode('utf-8')
        future = publisher.publish(topic_path, data=data)
        print('Published {} of message ID {}.'.format(data, future.result()))

    print('Published messages.')


def receive_messages(project_id, subscription_name):
    """Receives messages from a pull subscription."""
    # [START pubsub_subscriber_async_pull]
    # [START pubsub_quickstart_subscriber]
    import time

    from google.cloud import pubsub_v1

    # TODO project_id = "Your Google Cloud Project ID"
    # TODO subscription_name = "Your Pub/Sub subscription name"

    subscriber = pubsub_v1.SubscriberClient()
    # The `subscription_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/subscriptions/{subscription_name}`
    subscription_path = subscriber.subscription_path(
        project_id, subscription_name)

    def callback(message):
        print('Received message: {}'.format(message))
        message.ack()

    subscriber.subscribe(subscription_path, callback=callback)

    # The subscriber is non-blocking. We must keep the main thread from
    # exiting to allow it to process messages asynchronously in the background.
    print('Listening for messages on {}'.format(subscription_path))
    while True:
        time.sleep(60)


# create_topic("buho-platform","myTopic")

publish_messages("qwiklabs-gcp-0ba58ec53379f900","emeTopic")
# receive_messages("qwiklabs-gcp-0ba58ec53379f900","mysubAdamo")
