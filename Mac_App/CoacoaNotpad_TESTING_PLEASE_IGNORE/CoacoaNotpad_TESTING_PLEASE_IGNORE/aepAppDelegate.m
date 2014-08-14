//
//  aepAppDelegate.m
//  CoacoaNotpad_TESTING_PLEASE_IGNORE
//
//  Created by Alex Parson on 8/9/14.
//  Copyright (c) 2014 Cortex Storage. All rights reserved.
//

#import "aepAppDelegate.h"

@implementation aepAppDelegate

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification
{
    // Insert code here to initialize your application
}

- (IBAction)Mute:(id)sender {
    NSLog(@"MUTE");
}

- (IBAction)takeFloatValueForVolumeFrom:(id)sender {
    NSString *senderName = nil;
    if (sender == self.textfield){
        senderName = @"textField";
    }
    else {
        senderName = @"Slider";
    }
    NSLog(senderName, [sender floatValue]);
}
@end
