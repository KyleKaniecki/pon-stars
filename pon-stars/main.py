#!/usr/bin/env python

from db import DatabaseSession, Coupon, Store

if __name__ == '__main__':
    session = DatabaseSession()

    store = Store(store_type=1, zip_code='14586')
    session.add_model(store)

    store.coupons = [
        Coupon(brand='Samsung', discount=0.05)
    ]

    session.commit_changes()

