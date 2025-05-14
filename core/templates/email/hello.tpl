{% extends "mail_templated/base.tpl" %}

{% block subject %}
Accounts Activation
{% endblock %}

{% block html %}
{{ token }}
{% endblock %}