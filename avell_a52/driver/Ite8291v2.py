"""
Copyright (c) 2019, Petryx.
License MIT
Created on August 19, 2019
@author: @petryx
"""
import usb.core
import usb.util


class Ite8291v2():

    def __init__(self, vendor_id, product_id):
        self.vendor_id = vendor_id
        self.product_id = product_id
        """
        Parameters Collected by Reverse Engineering on Windows
        """
        self.bmRequestType = 0x21
        self.bRequest = 0x09
        self.wValue = 0x300
        self.wIndex = 1
        self.n_cols = 4
        self.getDevice()

    def getDevice(self):
        self.dev = usb.core.find(
            idVendor=self.vendor_id, idProduct=self.product_id)
        if self.dev is None:
            raise ValueError(
                "Device Not Found. Tip: use lsusb to find your device")
        if self.dev.is_kernel_driver_active(1):
            self.dev.detach_kernel_driver(1)
        # Get Active Configuration
        cfg = self.dev.get_active_configuration()

        self.in_ep = self._get_endpoint(cfg[(1, 0)], usb.util.ENDPOINT_IN)
        self.out_ep = self._get_endpoint(cfg[(1, 0)], usb.util.ENDPOINT_OUT)

    def _get_endpoint(self, intf, ep_type):

        ep = usb.util.find_descriptor(
            intf,
            custom_match=lambda e:
            usb.util.endpoint_direction(e.bEndpointAddress) ==
            ep_type)

        return ep

    def sendCommand(self, *payload):
        self.dev.ctrl_transfer(
            self.bmRequestType, self.bRequest, self.wValue, self.wIndex, payload)
