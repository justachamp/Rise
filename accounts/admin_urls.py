from django.conf.urls import patterns, url

from . import admin_views as views


urlpatterns = patterns('',
    url(r'^accounts/$', views.AccountListView.as_view(), name='admin_accounts'),
    url(r'^accounts/add/$', views.AccountCreateView.as_view(), name='admin_accounts_add'),
    url(r'^accounts/export/accounts/$', views.ExportAccountsView.as_view(), name='admin_accounts_export_accounts'),
    url(r'^accounts/export/users/$', views.ExportUsersView.as_view(), name='admin_accounts_export_users'),
    url(r'^accounts/export/invites/$', views.ExportInvitesView.as_view(), name='admin_accounts_export_invites'),
    url(r'^accounts/export/accounts/overfull$', views.ExportOverfullAccountsView.as_view(), name='admin_overfull_accounts_export'),
    url(r'^accounts/(?P<pk>\d+)/$', views.AccountDetailView.as_view(), name='admin_account'),
    url(r'^accounts/(?P<pk>\d+)/audit/$', views.AccountAuditView.as_view(), name='admin_account_audit'),
    url(r'^accounts/(?P<pk>\d+)/merge/$', views.AccountMergeView.as_view(), name='admin_account_merge'),
    url(r'^accounts/(?P<pk>\d+)/invitations/$', views.AccountInvitationView.as_view(), name='admin_account_invitations'),
    url(r'^accounts/(?P<pk>\d+)/credit-card/$', views.AccountCreditCardView.as_view(), name='admin_account_credit_card'),
    url(r'^accounts/(?P<pk>\d+)/bank-account/$', views.AccountBankAccountView.as_view(), name='admin_account_bank_account'),
    url(r'^accounts/(?P<pk>\d+)/bank-account/verify/$', views.AccountBankAccountVerifyView.as_view(), name='admin_account_bank_account_verify'),
    url(r'^accounts/bank-account/delete/(?P<pk>\d+)/(?P<card>\d+)/$', views.AccountDeleteBankAccountView.as_view(), name='admin_account_bank_account_delete'),
    url(r'^accounts/credit-card/delete/(?P<pk>\d+)/(?P<card>\d+)/$', views.AccountDeleteCreditCardView.as_view(), name='admin_account_credit_card_delete'),
    url(r'^accounts/billing/method/(?P<pk>\d+)/(?P<method>\d+)/$', views.DefaultPayMethodView.as_view(), name='default_payment_method'),
    url(r'^accounts/(?P<pk>\d+)/charges/$', views.AccountChargeListView.as_view(), name='admin_account_charges'),
    url(r'^accounts/(?P<pk>\d+)/charges/add/$', views.AccountChargeCreateView.as_view(), name='admin_account_charges_add'),
    url(r'^accounts/(?P<account_pk>\d+)/charges/(?P<pk>\d+)/$', views.AccountChargeDetailView.as_view(), name='admin_account_charge'),
    url(r'^accounts/(?P<account_pk>\d+)/charges/(?P<pk>\d+)/refund/$', views.AccountChargeRefundFormView.as_view(), name='admin_account_charge_refund'),
    url(r'^accounts/(?P<account_pk>\d+)/charges/(?P<pk>\d+)/void/$', views.AccountChargeVoidFormView.as_view(), name='admin_account_charge_void'),
    url(r'^accounts/(?P<pk>\d+)/edit/$', views.AccountUpdateView.as_view(), name='admin_account_edit'),
    url(r'^accounts/plans/contractchoices/$', views.ContractChoicesView.as_view(), name='plan_contract_choices'),
    url(r'^accounts/plans/contractchoices/separated$', views.ContractChoicesViewSeparateFields.as_view(), name='plan_contract_choices_separated'),
    url(r'^accounts/(?P<pk>\d+)/users/add/$', views.UserCreateView.as_view(), name='admin_account_add_user'),
    url(r'^accounts/(?P<account_pk>\d+)/users/(?P<pk>\d+)/$', views.UserDetailView.as_view(), name='admin_account_user'),
    url(r'^accounts/(?P<account_pk>\d+)/users/(?P<pk>\d+)/edit/$', views.UserUpdateView.as_view(), name='admin_account_user_edit'),
    url(r'^accounts/(?P<account_pk>\d+)/users/(?P<member_pk>\d+)/notes/$', views.UserNoteListView.as_view(), name='admin_account_user_notes'),
    url(r'^accounts/(?P<account_pk>\d+)/users/(?P<member_pk>\d+)/notes/(?P<pk>\d+)$', views.UserNoteDetailView.as_view(), name='admin_account_user_note_detail'),
    url(r'^accounts/(?P<account_pk>\d+)/users/(?P<member_pk>\d+)/notes/add/$', views.UserAddNoteView.as_view(), name='admin_account_user_add_note'),
    url(r'^accounts/(?P<pk>\d+)/reservations/$', views.AccountReservationListView.as_view(), name='admin_account_reservations'),
    url(r'^accounts/(?P<pk>\d+)/onboarding/$', views.AccountSendOnboardingEmailView.as_view(), name='admin_account_send_onboarding_email'),
    url(r'^accounts/(?P<account_pk>\d+)/users/(?P<pk>\d+)/welcome/$', views.UserSendWelcomeEmailView.as_view(), name='admin_user_send_welcome_email'),
    url(r'^accounts/(?P<account_pk>\d+)/users/(?P<pk>\d+)/password/$', views.UserUpdatePasswordView.as_view(), name='admin_user_password'),
    url(r'^accounts/(?P<account_pk>\d+)/users/(?P<pk>\d+)/password/reset/$', views.UserResetPasswordView.as_view(), name='admin_user_password_reset'),

    url(r'^users/$', views.UserListView.as_view(), name='admin_users'),
    url(r'^staff/$', views.StaffListView.as_view(), name='admin_staff'),
    url(r'^staff/oncallschedule$', views.OnCallScheduleView.as_view(), name='admin_oncall_schedule'),
    url(r'^staff/oncallschedule/create$', views.OnCallScheduleCreateView.as_view(), name='admin_oncall_schedule_create'),
    url(r'^staff/oncallschedule/(?P<pk>\d+)/delete$', views.OnCallScheduleDeleteView.as_view(), name='admin_oncall_schedule_delete'),
    url(r'^staff/user/add/$', views.StaffUserCreateView.as_view(), name='admin_staff_user_add'),
    url(r'^staff/user/(?P<pk>\d+)/$', views.StaffUserDetailView.as_view(), name='admin_staff_user_detail'),
    url(r'^staff/user/(?P<pk>\d+)/edit/$', views.StaffUserUpdateView.as_view(), name='admin_staff_user_edit'),
    url(r'^staff/origincity/flights', views.OriginCityFlights.as_view(), name='origin_city_flights'),
    # url(r'^staff/(?P<pk>\d+)/remove/$', views.StaffUserRemoveView.as_view(), name='admin_staff_user_remove'),
)
