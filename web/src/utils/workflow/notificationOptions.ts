export const notificationOptions = [
  {
    id: "notifications",
    type: "multiple-checkbox",
    options: [
      {
        id: "slack_thread_reply",
        type: "checkbox",
        group: "notification",
        label: "Get reply to the alert which triggered this workflow",
      },
      {
        id: "slack_message",
        label: "Send via Slack message",
        type: "checkbox",
        group: "notification",
      },
    ],
  },
];
