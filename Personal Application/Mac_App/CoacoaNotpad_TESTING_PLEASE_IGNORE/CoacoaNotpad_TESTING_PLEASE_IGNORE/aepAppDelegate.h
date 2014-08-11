//
//  aepAppDelegate.h
//  CoacoaNotpad_TESTING_PLEASE_IGNORE
//
//  Created by Alex Parson on 8/9/14.
//  Copyright (c) 2014 Cortex Storage. All rights reserved.
//

#import <Cocoa/Cocoa.h>

@interface aepAppDelegate : NSObject <NSApplicationDelegate>

@property (assign) IBOutlet NSWindow *window;
- (IBAction)Mute:(id)sender;
- (IBAction)takeFloatValueForVolumeFrom:(id)sender;
@property (weak) IBOutlet NSTextField *textfield;
@property (weak) IBOutlet NSSlider *slider;

@end
