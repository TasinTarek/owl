/** @odoo-module */

import { registry } from "@web/core/registry"
const { Component } = owl

export class OwlDashboard extends Component {}

OwlDashboard.template = "owl.OwlDashboard"

registry.category("actions").add("owl.dashboard", OwlDashboard)